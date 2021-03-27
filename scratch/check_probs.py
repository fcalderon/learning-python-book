die_1 = range(1,7)
die_2 = range(1,7)

results = {}

for n in die_1:
    for j in die_2:
        result = j + n
        if result not in results:
            results[result] = {
                'combinations': [],
                'combination_count': 0
            }

        results[result]['combinations'].append({"die_1": n, "die_2": j})
        results[result]['combination_count'] += 1

print(results)

sorted_values = list(results.keys())
sorted_values.sort()


for key in sorted_values:
    print(f'{key} - {results[key]["combination_count"]}')

def fibo(number):
    if number in [0, 1]:
        return number

    return fibo(number - 1) + fibo(number - 2)
