import json
import messages


class Record_Manager:

    def __init__(self, user, RESTRICTIONS):
        self.user = user
        self.restrictions = RESTRICTIONS

#-----------------------------------------------------RECORD VIEWER

    def view(self):
        try:
            with open("records.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messages.file_not_found()
        else:
            record = input("\nWhich record are you requesting access for? ")
            for title in data:
                if title.lower() == record.lower():
                    clearance_level = data[title]["Clearance Level"]
                    if self.user.clearance_check(clearance_level):
                        message_body = data[title]["Text"]
                        author = data[title]["Author"]
                        messages.show_record(title, message_body, author)
                    else:
                        messages.not_authorized()

#-----------------------------------------------------RECORD LIST

    def list(self):
        try:
            with open("records.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messages.file_not_found()
        else:
            for title in data:
                title_clearance = self.restrictions[data[title]
                                                    ["Clearance Level"]]
                print(f"{title}, {title_clearance}")

#-----------------------------------------------------RECORD CREATOR

    def create(self):
        title = input("\nEnter title of record: ")
        text = input("Enter the body of the record: ")
        input_validated = False

        while input_validated == False:
            clearance = input(
                f"Enter the Classification of this record\n"
                f"Note that you can only classify things up to your clearance level.\n"
                f"Your clearance level: {self.user.clearance_level}\n"
                f"0=Unclassified, 1=Restricted, 2=Classified, 3=Secret, 4=Forbidden: "
            )
            try:
                clearance = int(clearance)
            except ValueError:
                messages.invalid_value()
            else:
                input_validated = True

        if self.user.clearance_check(clearance):
            new_record = {
                title: {
                    "Text": text,
                    "Clearance Level": clearance,
                    "Author": f"{self.user.title} {self.user.name}",
                }
            }
            try:
                with open("records.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = new_record
            else:
                data.update(new_record)
            finally:
                with open("records.json", "w") as file:
                    json.dump(data, file, indent=4)
                    print("Record Created!")
        else:
            messages.not_authorized()
            print("Your record has been purged and you must resubmit.")


#-----------------------------------------------------REDACT RECORD

    def redact(self):
        redacted_records = 1
        try:
            with open("records.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            messages.file_not_found()
        else:
            record = input(
                "\nYour clearance level must be at least one level higher than the record to redact it.\nWhich record would you like to redact? "
            )

            for title in data:
                if f"REDACTED{redacted_records}" == title:
                    redacted_records += 1

            for title in data:
                if title.lower() == record.lower():
                    clearance_level = (data[title]["Clearance Level"]) + 1
                    if self.user.clearance_check(clearance_level):
                        is_sure = messages.redact()
                        if is_sure:
                            redacted_file = {
                                f"REDACTED{redacted_records}": {
                                    "Text": data[title]["Text"],
                                    "Clearance Level": 4,
                                    "Author": data[title]["Author"],
                                }
                            }

                            del data[title]
                            data.update(redacted_file)
                            with open("records.json", "w") as file:
                                json.dump(data, file, indent=4)
                                print("\n**REDACTED RECORD**\n")
                                break

                        else:
                            print("\n**File Not Redacted**\n")
                    else:
                        messages.not_authorized()
