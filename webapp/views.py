from django.shortcuts import render

# Create your views here.
history = []
turns = 0


def index_view(request):
    if request.method == 'POST':
        input_data = request.POST.get('numbers')
        secrets = [1, 2, 3, 4]
        try:
            numbers = list(map(int, input_data.split()))
            result = guess_numbers(secrets, numbers)
        except ValueError:
            result = "Enter 4 numbers"
        except KeyError:
            result = "Enter correct numbers"

        history.append(result)

        context = {
            'result': result
        }
        return render(request, 'result.html', context)
    else:
        return render(request, 'index.html')


def history_view(request):

    turns_history ={}
    for i in range(len(history)):
        turns_history[i+1] = history[i]

    context = {
        'index': len(history),
        'history': turns_history
    }

    return render(request, 'history.html', context)


def guess_numbers(secret, actual):
    if len(actual) != 4:
        raise ValueError

    for i in actual:
        if i >= 10 or i == 0:
            raise KeyError

    new_actual = set(actual)
    if len(new_actual) != 4:
        raise KeyError
    bulls = 0
    cows = 0
    for i in secret:
        for j in actual:
            if i == j:
                cows += 1
    i = 0
    for _ in secret:
        if secret[i] == actual[i]:
            bulls += 1
        i += 1
    cows = cows - bulls

    if bulls == 4:
        return "You got it right!"
    else:
        return f"You got {bulls} bulls, {cows} cows"
