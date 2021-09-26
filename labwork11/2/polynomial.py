"""
Implementation of the Polynomial ADT using a sorted linked list.
"""


class Polynomial:
    """
    Polynomial class.
    """
    # Create a new polynomial object.

    def __init__(self, degree=None, coefficient=None):
        if degree is None:
            self._poly_head = None
        else:
            self._poly_head = _PolyTermNode(degree, coefficient)
        self._poly_tail = self._poly_head

    # Return the degree of the polynomial.
    def degree(self):
        """
        Return the degree of the polynomial.
        """
        if self._poly_head is None:
            return -1
        return self._poly_head.degree

    # Return the coefficient for the term of the given degree.
    def __getitem__(self, degree):
        assert self.degree() >= 0, "Operation not permitted on an empty polynomial."
        cur_node = self._poly_head
        while cur_node is not None and cur_node.degree >= degree:
            cur_node = cur_node.next

        if cur_node is None or cur_node.degree != degree:
            return 0.0
        return cur_node.coefficient

    # Evaluate the polynomial at the given scalar value.
    def evaluate(self, scalar):
        """
        Evaluate the polynomial at the given scalar value.
        """
        assert self.degree() >= 0, "Only non -empty polynomials can be evaluated."
        result = 0.0
        cur_node = self._poly_head
        while cur_node is not None:
            result += cur_node.coefficient * (scalar ** cur_node.degree)
            cur_node = cur_node.next
        return result

    # Polynomial addition: new_poly = self + rhs_poly.
    def __add__(self, rhs_poly):
        assert self.degree() >= 0 and rhs_poly.degree() >= 0
        new_poly = Polynomial()
        node_a = self._poly_head
        node_b = rhs_poly._poly_head
        # Add corresponding terms until one list is empty.
        while node_a is not None and node_b is not None:
            if node_a.degree > node_b.degree:
                degree = node_a.degree
                value = node_a.coefficient
                node_a = node_a.next
            elif node_a.degree < node_b.degree:
                degree = node_b.degree
                value = node_b.coefficient
                node_b = node_b.next
            else:
                degree = node_a.degree
                value = node_a.coefficient + node_b.coefficient
                node_a = node_a.next
                node_b = node_b.next
            new_poly._append_term(degree, value)
        # If self list contains more terms append them.
        while node_a is not None:
            new_poly._append_term(node_a.degree, node_a.coefficient)
            node_a = node_a.next
        # Or if rhs contains more terms append them.
        while node_b is not None:
            new_poly._append_term(node_b.degree, node_b.coefficient)
            node_b = node_b.next

        return new_poly

    # Polynomial subtraction: new_poly = self - rhs_poly.
    def __sub__(self, rhs_poly):
        assert self.degree() >= 0 and rhs_poly.degree() >= 0
        new_poly = Polynomial()
        node_a = self._poly_head
        node_b = rhs_poly._poly_head
        # Add corresponding terms until one list is empty.
        while node_a is not None and node_b is not None:
            if node_a.degree > node_b.degree:
                degree = node_a.degree
                value = node_a.coefficient
                node_a = node_a.next
            elif node_a.degree < node_b.degree:
                degree = node_b.degree
                value = -node_b.coefficient
                node_b = node_b.next
            else:
                degree = node_a.degree
                value = node_a.coefficient - node_b.coefficient
                node_a = node_a.next
                node_b = node_b.next
            new_poly._append_term(degree, value)
        # If self list contains more terms append them.
        while node_a is not None:
            new_poly._append_term(node_a.degree, node_a.coefficient)
            node_a = node_a.next
        # Or if rhs contains more terms append them.
        while node_b is not None:
            new_poly._append_term(node_b.degree, -node_b.coefficient)
            node_b = node_b.next

        return new_poly

    # Polynomial multiplication: new_poly = self * rhs_poly.
    def __mul__(self, rhs_poly):
        assert self.degree() >= 0 and rhs_poly.degree() >= 0
        new_poly = Polynomial()
        node_a = self._poly_head
        while node_a is not None:
            node_b = rhs_poly._poly_head
            while node_b is not None:
                degree = node_b.degree + node_a.degree
                coefficient = node_b.coefficient * node_a.coefficient
                new_poly._append_term(degree, coefficient)
                node_b = node_b.next
            node_a = node_a.next
        return new_poly

    def simple_add(self, rhs_poly):
        """
        Simple add method.
        """
        new_poly = Polynomial()
        if self.degree() > rhs_poly.degree():
            max_degree = self.degree()

        i = max_degree
        while i >= 0:
            value = self[i] + rhs_poly[i]
            new_poly._append_term(i, value)
            i += 1
        return new_poly

    # Helper method for appending terms to the polynomial.
    def _append_term(self, degree, coefficient):
        if coefficient != 0.0:
            new_term = _PolyTermNode(degree, coefficient)
            if self._poly_head is None:
                self._poly_head = new_term
            else:
                self._poly_tail.next = new_term
            self._poly_tail = new_term

    def __str__(self):
        result = ''
        node_a = self._poly_head
        while node_a is not None:
            result += str(node_a.coefficient) + "x" + \
                "**" + str(node_a.degree) + '  '
            node_a = node_a.next
        return result


# Class for creating polynomial term nodes used with the linked list.
class _PolyTermNode(object):
    def __init__(self, degree, coefficient):
        self.degree = degree
        self.coefficient = coefficient
        self.next = None

    def __str__(self):
        """
        Prints the value stored in self.
        __str__: Node -> Str
        """
        return str(self.coefficient) + "x" + str(self.degree)
