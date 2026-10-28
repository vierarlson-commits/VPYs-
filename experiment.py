import json
import string
import secrets


class IdGenerator:
    @staticmethod
    def generate_id():
        available_ascii = string.ascii_letters + string.digits
        return "".join(secrets.choice(available_ascii) for _ in range(8))
        

class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def get_person_info(self):
        person_info = {
            "id": IdGenerator.generate_id(),
            "name": self.name,
            "age": self.age,
            "country": self.country
            } 
        return person_info


class BoardOfDirectors(Person):
    def __init__(self, name, age, country):
        super().__init__(name, age, country)

    def get_bod_info(self):
            return self.get_person_info()


class CEO(Person):
    def __init__(self, name, age, country):
        super().__init__(name, age, country)

    def get_ceo_info(self):
        return self.get_person_info()


class Employee(Person):
    def __init__(self, name, age, country, occupation):
        super().__init__(name, age, country)
        self.occupation = occupation

    def get_employee_info(self):
        employee_info = self.get_person_info() | {"occupation": self.occupation}
        return employee_info


class Company:
    def __init__(self, company_name, founded_year):
        self.company_name = company_name
        self.founded_year = founded_year

    def prepare_members_data(self, members: list):
        data  = {
            "ceo": {},
            "board of directors": [],
            "employees": []
        }

        for member in members:
            if isinstance(member, CEO):
                data["ceo"] = member.get_person_info()
                continue
            elif isinstance(member, BoardOfDirectors):
                data["board of directors"].append(member.get_person_info())
                continue
            elif isinstance(member, Employee):
                data["employees"].append(member.get_employee_info())
                continue
            else:
                raise TypeError(f"{member} is not a recognized company role")
            
        return data

    def members_json_data(self, company_members):
        members_data = self.prepare_members_data(company_members)
        json_data = {
            self.company_name: {
                "founded year": self.founded_year,
                "members": members_data
                }
            }
        return json_data


    def register_members_json_own(self, company_members: list, file):
        members_data = self.prepare_members_data(company_members)

        json_data = {
            self.company_name: {
                "founded year": self.founded_year,
                "members": members_data
            }
        }
        with open(file, "w", encoding="utf-8") as corpo_file:
            json.dump(json_data, corpo_file, indent=2, ensure_ascii=False)


  

john = BoardOfDirectors("John Weak",  45, "England")
lylia = BoardOfDirectors("Lylia Smith",  38, "USA")
aaron = BoardOfDirectors("Aaron Logal", 41, "Italia")

nikolas = CEO("Nikolas Mendy", 51, "Norway")

alex = Employee("Alex Hirsh", 23, "Russia", "ML developer")
sarah = Employee("Sarah Connor", 28, "Canada", "Data Scientist")
hiroshi = Employee("Hiroshi Tanaka", 31, "Japan", "DevOps Engineer")
elena = Employee("Elena Papadopoulos", 26, "Greece", "Frontend Developer")
mateo = Employee("Mateo Hernandez", 34, "Mexico", "Backend Developer")

arasaka = Company("Arasaka", 2011)

arasaka_data = arasaka.members_json_data([john, lylia, aaron, nikolas, alex, sarah, hiroshi, elena, mateo])


william = BoardOfDirectors("William Vance", 52, "UK")
clara = BoardOfDirectors("Clara Dupont", 46, "France")
kenji = BoardOfDirectors("Kenji Sato", 49, "Japan")

hans = CEO("Hans Gruber", 55, "Austria")

diego = Employee("Diego Alvarez", 27, "Spain", "Data Engineer")
yuki = Employee("Yuki Tanaka", 24, "Japan", "UX Designer")
amina = Employee("Amina Diop", 30, "Senegal", "QA Engineer")
lucas = Employee("Lucas Meyer", 29, "Germany", "Cloud Architect")
priya = Employee("Priya Sharma", 33, "India", "Product Manager")

militech = Company("Militech", 2014)

militech_data = militech.members_json_data([william, clara, kenji, hans, diego, yuki, amina, lucas, priya])

def into_one_file(file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump([arasaka_data, militech_data],f, indent=2)

into_one_file('json_data.json')