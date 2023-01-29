class Term:
    def __init__(self, coef: float() = 0, exp: int() = 0, next=None):
        self.coef = coef
        self.exp = exp
        self.next = None


class Polynomial:
    def __init__(self):
        self.head = None

    # print your polynomial
    def display(self):
        if (self.head == None):
            print("Empty Polynomial")

        else:
            print(" ", end="")
            temp = self.head
            while (temp != None):
                if (temp != self.head):
                    print("+", temp.coef, end="")
                else:
                    print(temp.coef, end="")

                if (temp.exp != 0):
                    print("x^", temp.exp, end=" ", sep="")

                temp = temp.next

            print(end="\n")

    # add a term to your polynomial
    def addTerm(self, coef: float(), exp: int()):
        if (self.head == None):
            self.head = Term(coef, exp, None)
        else:
            temp = self.head
            # location will be one node behind temp in iterration
            location = None
            # till temp is a node with smaller exp
            while (temp != None and temp.exp >= exp):
                location = temp
                temp = temp.next

            if (location != None and location.exp == exp):
                location.coef = location.coef + coef
            else:
                term = Term(coef, exp)
                # the given term is the largest term in our polynomial
                if (location == None):
                    term.next = self.head
                    self.head = term
                # the given array most be add in the middle of our polynomial
                else:
                    term.next = location.next
                    location.next = term

    def add(self, other):
        # result will contain the ''head'' to result and will be returned
        result = Term(0, 0)
        tail = result

        # first poly
        first = self.head
        # second poly
        second = other.head
        while (first != None or second != None):
            if (first == None):
                tail.next = second
                break

            elif (second == None):
                tail.next = first
                break

            elif (first.exp == second.exp):
                tail.next = Term(first.coef + second.coef, first.exp)
                first = first.next
                second = second.next

            elif (first.exp > second.exp):
                tail.next = Term(first.coef, first.exp)
                first = first.next

            elif (first.exp < second.exp):
                tail.next = Term(second.coef, second.exp)
                second = second.next

            tail = tail.next

        return result.next

    def sub(self, other):
        temppoly = Polynomial()
        second = other.head
        while (second != None):
            temppoly.addTerm(-1 * second.coef, second.exp)
            second = second.next

        return self.add(temppoly)

    # this function will be invoke to add
    # the coefficient of the elements
    # having same powerer from the resultant linked list
    def removeDuplicates(self):
        second = None
        dup = None
        first = self.head

        # Pick elements one by one
        while (first != None and first.next != None):
            second = first

            # Compare the picked element
            # with rest of the elements
            while (second.next != None):

                # If powerer of two elements are same
                if (first.exp == second.next.exp):

                    # Add their coefficients and put it in 1st element
                    first.coeff = first.coeff + second.next.coeff
                    dup = second.next
                    second.next = second.next.next

                else:
                    second = second.next

            first = first.next

    def multiply(self, other):
        result = Polynomial()
        first = self.head
        second = other.head
        while first != None:
            while second != None:
                coef = first.coef * second.coef
                exp = first.exp + second.exp

                result.addTerm(coef, exp)

                second = second.next

            second = other.head
            first = first.next

        result.removeDuplicates()
        return result.head

    def derivative(self):
        tail = self.head
        result = Term(0, 0)
        resulthead = result
        while (tail != None):
            result.next = Term(tail.coef * tail.exp, tail.exp - 1)
            result = result.next
            tail = tail.next

        return resulthead.next

    def integral(self):
        tail = self.head
        result = Term(0, 0)
        resulthead = result
        while (tail != None):
            result.next = Term((tail.coef / (tail.exp + 1)), tail.exp + 1)
            result = result.next
            tail = tail.next

        return resulthead.next

    def f_x_(self, x):
        answer = 0
        current = self.head
        while current:
            answer += current.coef * (x ** current.exp)
            current = current.next
        return answer