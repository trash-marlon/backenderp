from rest_framework.viewsets import ModelViewSet
from conf.api.serializers import ConfigurationSerializer
from rest_framework.permissions import IsAuthenticated
from conf.models import Configuration
# Load Models
from con.models.contact import Country

class ConfigurationViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ConfigurationSerializer
    queryset = Configuration.objects.all()

    def LoadData():
        try:
            conf = Configuration.objects.get(pk=1)
        except Configuration.DoesNotExist:
            print("load data from file csv")
            conf = Configuration()
            conf.id = 1
            conf.name = "Configuration"
            conf.uc_id = 1

            # Load all data from file csv
            # 1. Load country from data/country.csv
            csv =  open('con/data/country.csv', 'r')
            
            cont = 0    
            for line in csv:
                # skip first line becourse is header
                if cont == 0:
                    cont = 1
                    continue
                else:
                    cont += 1
                country = Country()
                country.name =  line.split(',')[0]
                country.code =  line.split(',')[1]
                country.uc_id = 1
                country.save()
            csv.close()
            conf.save()
    
    # call load data
    LoadData()