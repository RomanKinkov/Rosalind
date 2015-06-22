with open("d:\data\input.txt") as file:
    line = file.readline()
    a_count = line.count("A")
    c_count = line.count("C")
    g_count = line.count("G")
    t_count = line.count("T")

with open("d:\data\output.txt", "w") as file:
    file.write(str(a_count) + " " + str(c_count) + " " + str(g_count) + " " + str(t_count))
##comment это моё первое задание
