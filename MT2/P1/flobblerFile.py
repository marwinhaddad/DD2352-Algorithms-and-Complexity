from itertools import combinations

def checkFlobbler(n, m, k, tasks):
    for fired in combinations(range(1, m + 1), k):
        newTasks = []
        for i in range(n):
            keptEmployees = []
            for employee in tasks[i]:
                if employee not in fired:
                    keptEmployees.append(employee)
            newTasks.append(keptEmployees)

        count = 0
        for task in newTasks:
            if len(task) >= 3:
                count += 1

        if count == n:
            print(fired, 'are fired')
            return True
    print('Cannot fire k employees')
    return False



