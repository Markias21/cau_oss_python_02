import math

class Line:
    """
    길이를 받는 클래스이다. 
    """
    def __init__(self, length=1):
        """
        초기값을 설정하는 함수이다.
        """
       
        self.__length = length

    
    def set_length(self, length):
        """
        __length의 값을 length로 정한다.
        args: 
            length: 정해질 값
        return:
            아무 것도 리턴하지 않는다.
        """

        self.__length =length

    def get_length(self):
        """__length값을 리턴받는다.
        args: 없음
        returns: __length값을 반환받는다."""
        return self.__length
    



def area_square(line):
    """
    정사각형의 한 변의 길이를 받으면, 정사각형의 넓이를 리턴하는 함수이다. 단, 인수가 Line클래스 타입이 아니면 0을 반환한다.
    Args: 
        line:정사각형 한 변의 길이
    returns:
        int or float: 정사각형의 넓이를 반환한다."""
    if not isinstance(line, Line):
        return 0
    return line.get_length() **2




def area_circle(line):
    """
    원의 반지름을 받으면, 원의 넓이를 리턴하는 함수이다. 단, 인수가 Line클래스 타입이 아니면 0을 반환한다.
    Args:
        line: 원의 반지름의 길이
    returns:
        int or float: 원의 넓이를 반환한다."""
    if not isinstance(line, Line):
        return 0
    return line.get_length() **2 * math.pi




def area_regular_triangle(line):
    """
    정삼각형의 한 변의 길이를 받으면, 정삼각형의 넓이를 리턴하는 함수이다. 단, 인수가 Line클래스 타입이 아니면 0을 반환한다.
    Args:
        line: 정삼각형 한 변의 길이
    returns:
        int or float: 정삼각형의 넓이를 반환한다."""
    if not isinstance(line, Line):
        return 0
    return line.get_length()**2*math.sqrt(3)/4
