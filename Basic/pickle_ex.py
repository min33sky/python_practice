import _pickle


# profile_file = open("profile.pickle", "wb")

# profile = {"이름": "박명수", "age": 30, "취미": ["축구", "야구", "농구"]}

# print(profile)

# _pickle.dump(profile, profile_file)

# profile_file.close()


profile_file = open("profile.pickle", "rb")

profile = _pickle.load(profile_file)

print(profile)

profile_file.close()

