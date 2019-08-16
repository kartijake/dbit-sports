from django.shortcuts import render
from .models import men_100_meter,men_relay,men_Long_jump,men_javelin,men_discus,men_shot_put,men_1500_meter,men_800_meter,men_400_meter, men_200_meter
# Create your views here.
def event_results(request):
	m1001=men_100_meter.objects.get(id=1)
	m1002=men_100_meter.objects.get(id=2)
	m1003=men_100_meter.objects.get(id=3)
	

	#200 meters 
	m2001=men_200_meter.objects.get(id=1)
	m2002=men_200_meter.objects.get(id=2)
	m2003=men_200_meter.objects.get(id=3)

	#400 meters
	m4001=men_400_meter.objects.get(id=1)
	m4002=men_400_meter.objects.get(id=2)
	m4003=men_400_meter.objects.get(id=3)

	#800 meters
	m8001=men_800_meter.objects.get(id=1)
	m8002=men_800_meter.objects.get(id=2)
	m8003=men_800_meter.objects.get(id=3)

	#1500 meters
	m15001=men_1500_meter.objects.get(id=1)
	m15002=men_1500_meter.objects.get(id=2)
	m15003=men_1500_meter.objects.get(id=3)

	#short put
	st1=men_shot_put.objects.get(id=1)
	st2=men_shot_put.objects.get(id=2)
	st3=men_shot_put.objects.get(id=3)

	#discus throw
	dt1=men_discus.objects.get(id=1)
	dt2=men_discus.objects.get(id=2)
	dt3=men_discus.objects.get(id=3)

	#javelin throw
	jt1=men_javelin.objects.get(id=1)
	jt2=men_javelin.objects.get(id=2)
	jt3=men_javelin.objects.get(id=3)



	#long jump 
	lj1=men_Long_jump.objects.get(id=1)
	lj2=men_Long_jump.objects.get(id=2)
	lj3=men_Long_jump.objects.get(id=3)
	
	#4X 100 mts men
	r1=men_relay.objects.get(id=1)
	r2=men_relay.objects.get(id=2)
	r3=men_relay.objects.get(id=3)



	dic={'object1':m1001,"object2":m1002,"object3":m1002,'mm21':m2001,'mm22':m2002,"mm23":m2003,'mm41':m4001,'mm42':m4002,'mm43':m4003,
	'mm81':m8001,"mm82":m8002,'mm83':m8003,'mm151':m15001,'mm152':m15002,'mm153':m15003,'ms1':st1,'ms2':st2,"ms3":st3,'md1':dt1,'md2':dt2,
	'md3':dt3,'mj1':jt1,'mj2':jt2,'mj3':jt3,"ml1":lj1,'ml2':lj2,'ml3':lj3,'mr1':r1,"mr2":r2,"mr3":r3}
	
	return render(request,'results.html',dic)