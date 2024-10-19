from main import Character
character =  Character(data_folder='link to you data folder')

if __name__ =="__main__":
    character =  Character(data_folder='link to you data folder')
    while True:
        inp = input("Enter the prompt: ")
        response = character.get_response(message=f"{inp}")
        print(f"Your Character Name: {response}")


