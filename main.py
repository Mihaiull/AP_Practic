from Infrastructure.Repo import Repo

repo=Repo()
repo.add(3,5,20)
repo.add(4,5,21)
repo.add(5,5,22)
repo.add(6,8,23)
repo.add(7,9,4)


while(True):
    try:
        print(repo)
        print('1. Add a measurement')
        print('2. Get all measurements with pressure higher than a given value')
        print('3. Get the average pressure for a given hour')
        print('0. Exit')
        x=input('Enter your choice: ')
        print('\n\n')
        if x=='1':
            pressure=int(input('Enter pressure: '))
            hour=int(input('Enter hour: '))
            temperature=int(input('Enter temperature: '))
            repo.add(pressure, hour, temperature)
        elif x=='2':
            val=int(input('Enter value: '))
            print(repo.getpress(val))
            print('\n\n')
        elif x=='3':
            hour=int(input('Enter hour: '))
            print(repo.getavg(hour))
        elif x=='print':
            print(repo)
        elif x=='0':
            break
        else:
            print('Invalid command')
    except ValueError as e:
        print(e)
    except Exception as e:
        print(e)