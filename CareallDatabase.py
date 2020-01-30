import sqlite3
connection = sqlite3.connect('careall.db')

cursor = connection.cursor()

create_query = "CREATE TABLE `elder_details` (`Id` int(11) ,`Name` varchar(20) NOT NULL,`Age` int(3) NOT NULL,`Fund_raised` int(8) NOT NULL,`Contact` bigint(10) NOT NULL,`Taken_care_by` int(5) NOT NULL DEFAULT 0,`Request_id` int(3) NOT NULL DEFAULT 0,`Review` text DEFAULT NULL,`Rating` int(11) DEFAULT NULL) ;"

cursor.execute(create_query)

create_query = "INSERT INTO `elder_details` (`Id`, `Name`, `Age`, `Fund_raised`, `Contact`, `Taken_care_by`, `Request_id`, `Review`, `Rating`) VALUES(1, 'Ariya', 70, 20000, 8824547824, 0, 0, NULL, NULL),(2, 'Rohit', 65, 25000, 7321999579, 0, 0, NULL, NULL),(3, 'Devesh', 53, 10000, 8543208746, 1, 0, NULL, NULL),(4, 'jayesh', 61, 12000, 9123951591, 0, 0, NULL, NULL),(5, 'Himanshu', 67, 21000, 787449875, 0, 0, NULL, NULL),(6, 'Vinayak', 74, 22000, 8633313975, 0, 0, NULL, NULL),(7, 'shreyas', 59, 27000, 9632512876, 0, 0, NULL, NULL),(7, 'mayank', 72, 20000, 9658741354, 2, 0, NULL, NULL),(8, 'mohit', 64, 15000, 1245789654, 0, 3, NULL, NULL),(9, 'akansha', 68, 15000, 8745123654, 0, 0, NULL, NULL),(9, 'Arihant', 74, 10000, 7791071961, 0, 2, NULL, NULL); "

cursor.execute(create_query)

create_query = "CREATE TABLE `taking_care` (`youth_id` int(11) NOT NULL,`old_id_1` int(11) DEFAULT NULL,`old_id_2` int(11) DEFAULT NULL, `old_id_3` int(11) DEFAULT NULL,`old_id_4` int(11) DEFAULT NULL);"

cursor.execute(create_query)

create_query = "INSERT INTO `taking_care` (`youth_id`, `old_id_1`, `old_id_2`, `old_id_3`, `old_id_4`) VALUES(2, 10, 0, 0, 0);"

cursor.execute(create_query)


create_query ="CREATE TABLE `youth_details` (`Id` int(11) NOT NULL,`Name` varchar(20) NOT NULL,`Age` int(3) NOT NULL,`Address` varchar(100) NOT NULL,`Contact` bigint(10) NOT NULL,`Number_undertaken_elders` int(1) NOT NULL DEFAULT 0,`Review` text DEFAULT NULL,`Rating` int(11) DEFAULT NULL);"

cursor.execute(create_query)

create_query ="INSERT INTO `youth_details` (`Id`, `Name`, `Age`, `Address`, `Contact`, `Number_undertaken_elders`, `Review`, `Rating`) VALUES(1, 'Kiran', 20, 'Durga,Kothrud', 9874465478, 0, NULL, NULL),(2, 'Amit', 30, 'Kajraj,Pune', 9873256519, 1, NULL, NULL),(3, 'Aditya', 28, 'Balaji nagar,Pune', 8524478324, 0, NULL, NULL),(4, 'Chilli', 30, 'Lalghati nagar', 8745369875, 0, NULL, NULL);"
cursor.execute(create_query)

connection.commit()
connection.close()