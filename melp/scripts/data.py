from core.models import Restaurant
import csv


def run():
    with open('core/restaurantes.csv', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header

        Restaurant.objects.all().delete()

        for row in reader:
            print(row)

            restaurant = Restaurant(rating=row[1],
                        name=row[2],
                        site=row[3],
                        email=row[4],
                        phone=row[5],
                        street=row[6],
                        city=row[7],
                        state=row[8],
                        lat=row[9],
                        lng=row[10],
                        )
            restaurant.save()

if __name__ == "__main__":
    run()