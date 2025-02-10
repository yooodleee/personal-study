from django.core.paginator import EmptyPage, Paginator
from django.db.models import Subquery, OuterRef, Value
from django.db.models.functions import Coalesce

from cart.entity.cart import Cart
from cart.repository.cart_repository import CartRepository
from books.entity.books import Books


class CartRepositoryImpl(CartRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        
        return cls.__instance
    
    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        
        return cls.__instance
    
    def save(self, cart):
        try:
            if cart.getId():
                existingCart = Cart.objects.get(id=cart.id)
                existingCart.quantity = cart.quantity   # 수량 업데이트
                existingCart.save()
                return existingCart
            
            newCart = Cart.objects.create(
                account = cart.account,
                bookName = cart.bookName,
                quantity = cart.quantity,
            )
            return newCart
        except Exception as e:
            print(f"장바구니 저장 중 오류 발생: {e}")
            raise
    
    def findCartByAccountAndBookName(self, account, bookName):
        try:
            cart = Cart.objects.get(
                account = account,
                bookName = bookName,
            )
            return cart
        
        except Cart.DoesNotExist:
            print("오류: 조건에 만족하는 장바구니가 여러 개 존재합니다.")
            return None
        
        except Exception as e:
            print(f"장바구니 조회 중 오류 발생: {e}")
            return None
    
    def findCartByAccount(self, account, page, limit):
        try:
            # Cart 객체 필터링
            cartQueryset = Cart.objects.filter(account = account)

            # 가격 및 제목 먼저 annotate()로 처리
            annotatedCartQueryset = cartQueryset.annotate(
                price = Coalesce(
                    Subquery(
                        Books.objects.filter(
                            bookPrice = OuterRef("bookPrice")
                        ).values('bookPrice')[:1]
                    ),
                    Value(0),
                ),
                bookName = Coalesce(
                    Subquery(
                        Books.objects.filter(
                            bookName = OuterRef("bookName")
                        ).values("bookName")[:1]
                    ),
                    Value(""),
                ),
            )

            # Paginator로 페이지네이션 적용
            paginator = Paginator(
                annotatedCartQueryset, limit
            )   # limit을 페이지 크기로 설정

            try:
                paginateCart = paginator.page(page) # page는 페이지 번호
            except EmptyPage:
                # 잘못된 페이지 번호로 접근 시 마지막 페이지 반환
                paginateCart = paginator.page(paginator.num_pages)
            
            return paginateCart # 페이지 객체 반환
        
        except Exception as e:
            print(f"장바구니 조회 중 오류 발생: {e}")
            return []
    
    def findById(self, cartId):
        try:
            cart = Cart.objects.get(id=cartId)
            return cart
        except Cart.DoesNotExist:
            print(f"id {cartId} 존재하지 않음.")
            return None
        except Exception as e:
            print(f"Cartrepository.findById 에러: {e}")
            return None
    
    def deleteById(self, cartId):
        try:
            cart = Cart.objects.filter(id=cartId).first()
            if not cart:
                return False
            cart.delete()
            return True
        except Exception as e:
            print(
                f"Error in CartRepository.deleteById: {e}"
            )
            return False