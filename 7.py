s_hectare_ = int(input("Введите площадь в гектарах: "))
h_down_sm = 1
h_down_m = h_down_sm / 100
v_rain_l = s_hectare_ * h_down_m * 1000
print(v_rain_l)
