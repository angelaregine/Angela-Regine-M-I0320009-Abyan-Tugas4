usia = int(input("Berapa usia kamu:"))
ujian = input("Apakah anda sudah lulus ujian kualifikasi (Y/T):")

if usia  >= 21 and ujian == "Y":
    print("Anda dapat mendaftar di kursus")
else:
    print("Anda tidak dapat mendaftar di kursus")