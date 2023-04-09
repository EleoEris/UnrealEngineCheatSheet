
# untested - case insensitive
def getActorsByNames(*args) -> [actor]:
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        if any(string.lower() in lightActor.get_name().lower() for string in *args):
            yield actor
# tested - single line for editor
# [lightActor for lightActor in unreal.EditorLevelLibrary.get_all_level_actors() if any(string.lower() in lightActor.get_name().lower() for string in ["skylight", "skyatmosphere", "directionallight", "exponentialheightfog"])]

# untested
def getActorsByNamesCS(*args) -> [actor]:
    for actor in unreal.EditorLevelLibrary.get_all_level_actors():
        if any(string in lightActor.get_name().lower() for string in *args):
            yield actor

# untested
def moveAtmosphereUp():
    for actor in getActorsByNames("skylight", "skyatmosphere", "directionallight", "exponentialheightfog"):
        actor.set_actor_location(unreal.Vector(0, 0, 3000+(100*i)), False, True)

# tested - single line for editor:
# for i, actor in enumerate([lightActor for lightActor in unreal.EditorLevelLibrary.get_all_level_actors() if any(string.lower() in lightActor.get_name().lower() for string in ["skylight", "skyatmosphere", "directionallight", "exponentialheightfog"])]): actor.set_actor_location(unreal.Vector(0, 0, 3000+(100*i)), False, True)
