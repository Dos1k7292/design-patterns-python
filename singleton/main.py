from configuration_manager import ConfigurationManager
import threading


def test_singleton():
    config = ConfigurationManager()
    config.set_setting("AppName", "MyPythonApp")

    print("Thread:", threading.current_thread().name)
    print("ID:", id(config))
    print("AppName:", config.get_setting("AppName"))


t1 = threading.Thread(target=test_singleton)
t2 = threading.Thread(target=test_singleton)

t1.start()
t2.start()

t1.join()
t2.join()
