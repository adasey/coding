"""
    N×N의 이차원 배열 A가 있고, A의 각 원소는 -100부터 100 사이의 임의의 정수 값을 갖는다. 이 이차원 배열의 A[1][1]부터 시작하여 A[N][N]에 이르는 경로를 선택하려 하는데, 아래와 같은 제약 조건이 있다.

    상하좌우로 인접한 원소들을 방문해 나가야 한다. 즉 왼쪽, 오른쪽, 위쪽, 아래쪽의 네 가지 이동이 가능하다. 대각선으로는 이동이 불가능하다.
    한 번 방문한 원소는 다시 방문할 수 없다.
    이러한 제약을 만족하면서 임의의 경로를 따라 A[N][N]에 이르면 이 경로 상에 방문되었던 원소들의 값의 총합이 그 경로의 점수가 된다. 임의의 N×N 이차원 배열이 주어질 때, A[1][1]에서 A[N][N]에 이르는 경로의 점수를 최대화하는 프로그램을 작성하시오.

    입력
    첫째 줄에는 이차원 배열의 크기를 나타내는 정수 N(3≤N≤100)이 주어진다. 다음 N개의 줄에는 각각의 N개의 정수(-100이상 100이하)가 빈 칸을 사이에 두고 주어지는데, 둘째 줄에는 A[1][1]～A[1][N], 셋째 줄에는 A[2][1]～A[2][N], … , N+1번째 줄에는 A[N][1]～A[N][N]의 값이 주어진다.

    출력
    첫째 줄에 프로그램이 구한 경로의 점수를 출력한다. 둘째 줄에는 이동 경로를 나타내는 문자들을 빈 칸을 사이에 두고 출력한다. 왼쪽은 L, 오른쪽은 R, 위쪽은 U, 아래쪽은 D로 나타내며, A[1][1]에서부터의 이동을 순서대로 출력하면 된다.
"""
U_L = -1
D_R = 1
UP = "u"
DOWN = "d"
LEFT = "l"
RIGHT = "r"

typed = int(input())


class Route():
    path = []
    path_before = []
    total_score = 0

    def __init__(self):
        self.path_now_x, self.path_now_y = 0, 0
        self.next_x, self.next_y = None, None

    def pathInsert(self, road):
        self.path.append(road)

    def searchingPath(self):
        no_search = self.notSearch()
        before_pathed = self.checkFourDirection()

        if before_pathed in [UP, DOWN, RIGHT, LEFT]:
            if no_search:
                if no_search in "XY":
                    no_search = self.whichCorner()

                    if no_search in "s":
                        print(no_search)

                    elif no_search in "ur":
                        print(no_search)

                    elif no_search in "dl":
                        print(no_search)

                    else:
                        print(no_search)

                elif no_search in "x":
                    if no_search in "0":
                        print(no_search)

                    else:
                        print(no_search)

                else:
                    if no_search in "0":
                        print(no_search)

                    else:
                        print(no_search)

            else:
                print(no_search)
                print("False")

        else:
            if no_search:
                if no_search in "XY":
                    no_search = self.whichCorner()

                    if no_search in "s":
                        print(no_search)

                    elif no_search in "ur":
                        print(no_search)

                    elif no_search in "dl":
                        print(no_search)

                    else:
                        print(no_search)

                elif no_search in "x":
                    if no_search in "0":
                        print(no_search)

                    else:
                        print(no_search)

                else:
                    if no_search in "0":
                        print(no_search)

                    else:
                        print(no_search)

            else:
                print(no_search)
                print("False")

    def checkFourDirection(self):
        x = self.path_now_x
        y = self.path_now_y

        up_x = x + U_L
        down_x = x + D_R

        left_y = y + U_L
        right_y = y + D_R

        result = []

        try:
            up = self.toString(up_x, y)

            if self.isWalkBefore(up):
                result.append(UP)

            else:
                raise IndexError

        except:
            result.append(" ")

        try:
            down = self.toString(down_x, y)

            if self.isWalkBefore(down):
                result.append(DOWN)

            else:
                raise IndexError

        except:
            result.append(" ")

        try:
            left = self.toString(x, left_y)

            if self.isWalkBefore(left):
                result.append(LEFT)

            else:
                raise IndexError

        except:
            result.append(" ")

        try:
            right = self.toString(x, right_y)

            if self.isWalkBefore(right):
                result.append(RIGHT)

            else:
                raise IndexError

        except:
            result.append(" ")

        return result

    def toString(self, pos_x, pos_y):
        return str(pos_x) + "," + str(pos_y)
        
    def notSearch(self):
        if (self.path_now_x <= 0 or self.path_now_x >= typed) and (self.path_now_y <= 0 or self.path_now_y >= typed):
            return "XY" # side 4 corner
        
        else:
            if self.path_now_x <= 0 or self.path_now_x >= typed:
                if self.path_now_x <= 0:
                    return "x_0" # left side

                else:
                    return "x_t" # right side

            if self.path_now_y <= 0 or self.path_now_y >= typed:
                if self.path_now_y <= 0:
                    return "y_0" # up side
                
                else:
                    return "y_t" # down side

        return ""

    def whichCorner(self):
        """
            whichCorner -> four side corner of String
                    s : start 
                    ur : second right corner 
                    dl : third down left corner 
                    dr : last down right corner
        """
        if self.path_now_x <= 0 and self.path_now_y <= 0:
            return "s" # start

        elif self.path_now_x <= 0 and self.path_now_y >= typed:
            return "ur" # up right

        elif self.path_now_x >= typed and self.path_now_y <= 0:
            return "dl" # down left

        else:
            return "dr" # down right

    def isWalkBefore(self, pos):
        try:
            if pos in self.path_before:
                return True
        
        except:
            return False


def typingPath(path_count):
    route = Route()

    for _ in range(path_count):
        route.pathInsert(splitAndInt(input()))

    route.searchingPath()
    print(route.total_score)

def splitAndInt(list):
    return [int(a) for a in list.split()]

def testPrint(route):
    print(route)

typingPath(typed)