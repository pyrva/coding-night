# String calculator

Tonight, we will practice our crafe, and hopefully learn from each other as we go.

This will be a timed event. We will have 30 minutes to work on what we can, and then we'll come back together to discuss what we learned. We can continue after that if we'd like.

You will use tests to drive your code. Some people will use ``unittest``, some ``pytest``, and others will just run the code themselves. If possible, try using either ``unittest`` or ``pytest``. But I totally get it if you just aren't there yet.

## Keep these things in mind:

- Try not to read ahead

- Do one task at a time. The trick is to learn incrementally

- Make sure you only test for correct inputs. There is no need to test for invalid inputs for this kata.

- Don't worry about trying to complete this challenge in the 30 minutes. The point is to try to do what you can and to learn from everyone. We grow by stretching out further than we normally go, resting, and taking in what others have done.

- If you're confused, ask Chris for help. He'd be happy to help.

- Tell Chris if there's something that you think might make this more fun.

- Start with the simplest test case of an empty string and move to one and two numbers

- Try to solve things as simply as possible so that you force yourself to write tests you did not think about

- Try to refactor after each passing test


## Tonight's problem

1. Create a function called ``calculate`` that can take a string with up to two numbers, separated by commas, and will return their sum.

	- For example, “” or “1” or “1,2” are inputs. An empty string will return 0

————————————————————————————————


2. Allow ``calculate`` to handle an unknown amount of numbers

————————————————————————————————


3. Allow ``calculate`` to handle new lines between numbers (instead of commas).

	1. the following input is ok: “1\n2,3” (will equal 6)

	2. the following input is NOT ok: “1,\n” (not need to prove it - just clarifying)

————————————————————————————————


4. Support different delimiters

    to change a delimiter, the beginning of the string will contain a separate line that looks like this: “//[delimiter]\n[numbers…]” for example “//;\n1;2” should return three where the default delimiter is ‘;’ .

    the first line is optional. all existing scenarios should still be supported


————————————————————————————————


5. Calling ``calculate``  with a negative number will throw an exception “negatives not allowed” - and the negative that was passed. 

	- if there are multiple negatives, show all of them in the exception message.

————————————————————————————————

STOP HERE if you are a beginner. Continue if you can finish the steps so far in less than 30 minutes.

————————————————————————————————

6. Numbers bigger than 1000 should be ignored, so adding 2 + 1001 = 2

————————————————————————————————

7. Delimiters can be of any length with the following format: ``//[delimiter]\n`` for example: ``//[***]\n1***2***3`` should return ``6``

————————————————————————————————

8. Allow multiple delimiters like this: ``//[delim1][delim2]\n`` for example ``//[*][%]\n1*2%3`` should return 6.

————————————————————————————————

9. make sure you can also handle multiple delimiters with length longer than one char











	