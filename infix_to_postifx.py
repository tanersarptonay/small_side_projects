def infix_to_postfix(whole_op):

    """
    Infix to postfix converter
    :param whole_op: (str) An infix operation without whitespaces
    :return: postix operation
    """

    pre = {"+": 1, "-": 1, "*": 2, "/": 2, "^": 3, "(": -1, ")": 0}  # pre stands for precedence #
    assoc = {"+": "lr", "-": "lr", "*": "lr", "/": "lr", "^": "rl", "(": "n", ")": "n"}  # assoc stands for associativity #
    postfix = []
    stack = []

    for token in whole_op:
        if token not in pre:
            postfix.append(token)
        elif token == "(":
            stack.append(token)
        elif token == ")":
            while pre[token] < pre[stack[-1]]:
                postfix.append(stack[-1])
                stack.pop()
            if pre[token] > pre[stack[-1]]:
                stack.pop()

        else:   # if it is an operator#

            if len(stack) > 0 and pre[token] < pre[stack[-1]]:
                while len(stack) > 0 and pre[token] < pre[stack[-1]]:
                    postfix.append(stack[-1])
                    stack.pop()

            if len(stack) > 0 and pre[token] == pre[stack[-1]]:
                if (assoc[token] == "lr") and (assoc[stack[-1]] == "lr"):
                    while len(stack) > 0 and assoc[stack[-1]] == "lr" and (pre[token] == pre[stack[-1]]):
                        postfix.append(stack[-1])
                        stack.pop()
                stack.append(token)

            if len(stack) > 0 and pre[token] > pre[stack[-1]]:
                stack.append(token)

            if len(stack) == 0:  # if stack is empty
                stack.append(token)

    while len(stack) > 0:
        postfix.append(stack[-1])
        stack.pop()

    str_postfix = " ".join([str(token) for token in postfix])

    return str_postfix











