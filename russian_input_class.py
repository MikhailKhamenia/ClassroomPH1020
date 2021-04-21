class Ввод():
	def __call__(self, *args, **kwargs):
		return input(*args, **kwargs)

def печать(*args, **kwargs):
    return print(*args, **kwargs)
	    

def main():
    ввод_имени=Ввод()
    ввод_возраста=Ввод()
    имя=ввод_имени("ВВод имени")
    лет=ввод_возраста("Сколько лет")
    печать(f"Привет {имя}, вам {лет} лет")

if __name__=="__main__":main()
