from abc import ABC, abstractmethod


class BookmarkService(ABC):
    @abstractmethod
    # 메서드명을 보니 북마크를 등록할 것 같네요.
    # 생각해봅시다. 북마크를 등록하려면 당연히 북마크에 대한 정보(그 북마크가 언제 등록되었는지, 누가 등록한 것인지 등)
    # 에 대한 정보가 필요할 것이고, 북마크를 만든 사용자에 대한 정보가 필요할 것이므로 Id도 가져와줍니다.
    def bookmarkRegister(self, bookmarkData, accountId):
        pass

    @abstractmethod
    # 북마크 리스트를 가져올 메서드이지만 인자가 이상하네요.
    # 일단 pass할게요
    def bookmarkList(self, accountId):
        pass

    @abstractmethod
    # 사용자가 북마크를 북마크 리스트에서 해제하는 기능도 필요할 것 같아서
    # 북마크를 제거하는 함수도 만들어봤습니다.
    def removeBookmarkItem(self, bookmarkItemId):
        pass