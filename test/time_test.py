from time_ir import Time

t = Time()

print("تاریخ :")
print(f"تاریخ شمسی : {t.shamsi()}")
print(f"تاریخ میلادی : {t.miladi()}")
print(f"تاریخ قمری : {t.ghamari()}")
print(f"برج فلکی : {t.borjfalaki()}")

print("اوقات شرعی به افق تهران :")
print(f"اذان صبح : {t.azan_sobh()}")
print(f"طلوع خورشید : {t.tolo_khorshid()}")
print(f"اذان ظهر : {t.azan_zohr()}")
print(f"غروب خورشید : {t.ghrob_khorshid()}")
print(f"اذان مغرب : {t.azan_maghreb()}")
print(f"نیمه شب شرعی : {t.nime_shab()}")
