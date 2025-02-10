import multiprocessing

from user_defined_queue.repository.user_defined_queue_repository import UserDefinedQueueRepository


class UserDefinedQueueRepositoryImpl(UserDefinedQueueRepository):
    """
    Params
    -------------------------------
        __instace: 
            싱글턴 선언
        __systemSocketReceiveFastAPIChannel
        __systemFastAPISocketTransmitterChannel
    """
    __instance = None

    __systemSocketReceiverFastAPIChannel = None
    __systemFastAPISocketTransmitterChannel = None


    def __new__(cls):
        """
        classmethod 객체가 없다면 새로운 classmethod 객체를 생성하고 반환합니다.
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


    @classmethod
    def getInstance(cls):
        """
        * classmethod:
            전역 변수에서 선언한 싱글턴을 사용하려면 @classmethod를 사용합니다.
        """
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance


    def getUserDefinedSocketReceiverFastAPIChannel(self):
        """


        Return
        ------------
            __systemSocketReceiverFastAPIChannel:
                사용자 정의 SocketReceiverFastAPIChannel 정보를 가져옵니다.
        """

        return self.__systemSocketReceiverFastAPIChannel


    def getUserDefinedFastAPISocketTransmitterChannel(self):
        """


        Return
            __systemFastAPISocketTransmitterChannel:
                사용자 정의 FastAPISocketTransmitterChannel 정보를 가져옵니다.
        """

        return self.__systemFastAPISocketTransmitterChannel


    def create(self):
        """

        Params
        -------------
            __systemSocketRecieverFastAPIChannel:
                multiprocessing의 Queue로 해당 정보를 담는다. queue에 데이터 삽입
            __systemFastAPISocketTransmitterChannel:
                multiprocessing의 Queue로 해당 정보를 담는다. queue에 데이터 삽입
        """
        self.__systemSocketReceiverFastAPIChannel = multiprocessing.Queue()

        self.__systemFastAPISocketTransmitterChannel = multiprocessing.Queue()
    