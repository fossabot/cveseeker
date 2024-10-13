from services.api.sources.exploitdb import ExploitDBAPI
from services.api.sources.nist import NistAPI
from services.api.sources.opencve import OpenCVEAPI
from services.api.sources.packetstormsecurity import PacketStormSecurityAPI
from services.search_manager import SearchManager

class SearchProvider():
    def __init__(self):
        self.search_service: SearchManager = None
        
    def make_service_api(self) -> SearchManager:
        if self.search_service == None:
            self.boot()
            
        return self.search_service
    
    def boot(self):
        providers = [
            NistAPI(),
            PacketStormSecurityAPI(),
            OpenCVEAPI(),
            ExploitDBAPI()
        ]

        self.search_service = SearchManager(providers)