from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository()
    
    def get_actors(self):
        return self.actor_repository.get_actors() 
    
    def create_actor(self, name, birthday, nationality):
        actor = dict(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        return self.actor_repository.create_actor(actor)
    
    def update_actor(self, actor):
        return self.actor_repository.update_actor(actor)
    
    def delete_actor(self, actor):
        return self.actor_repository.delete_actor(actor['id'])
    