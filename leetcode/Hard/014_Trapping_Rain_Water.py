# The objective behind this algorithm is to use a stack of non-increasing elements
# and whenever we encounter an element that cannot be in a stack. Then
# we found the closest element that is larger than or equal to that element in consideration
# Then we add the difference between elements in between the minimum of that element larger and
# the element in consideration into the water variable, and we make all elements in between that min
def trapping_rain_water(inp: list[int]) -> int:
    stack = []
    water = 0 # where the differences would be added
    i = 0

    while i < len(inp):
        print("Before ==> " + str(stack))
        if i == 0: # if the stack is empty, hence we simply append the element
            stack.append(inp[i])
        elif (i > 0) and (stack[-1] >= inp[i]): # if the number is smaller than or equal to the closest elem
            stack.append(inp[i])
        else:
            l = len(stack) - 1
            while (l > 0) and stack[l] <= inp[i]: # finding the closest element smaller than this
                l -= 1
            height = min(stack[l], inp[i]) # finding the minimum in between this and that element larger than or equal to this

            h = len(stack) - 1 # then we decrement again from the closest element
            while (h > l) and (stack[h] <= height):
                water += (height - stack[h]) # adding the difference between 'height' and the stack[h]
                stack[h] = height # making the element 'height', since the difference has been added
                h -= 1

            if inp[i] > height: # if the element that was larger than or equal to was larger, which means we
                stack = [inp[i]]  # we must create a new stack from inp[i]
            else:
                stack.append(inp[i]) # else simply append this value

        print("After ==> " + str(stack) + "\n\n")
        i += 1

    return water # all the water that has been added

print(trapping_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
