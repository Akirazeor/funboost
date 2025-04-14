import time

from funboost import BrokerEnum, boost,FunctionResultStatusPersistanceConfig
import kombu

@boost('test_kombu2b', broker_kind=BrokerEnum.KOMBU, qps=0.1,
       function_result_status_persistance_conf=FunctionResultStatusPersistanceConfig(True,True),
       broker_exclusive_config={
           'kombu_url': 'redis://192.168.64.151:6378/10',
           'transport_options': {
               'visibility_timeout': 600, 'ack_emulation': True
           },
           'prefetch_count': 1000},log_level=20)
def f1(x, y):
    print(f'start {x} {y} 。。。')
    time.sleep(60)
    print(f'{x} + {y} = {x + y}')
    print(f'over {x} {y}')


if __name__ == '__main__':
    # f1.push(3,4)
    print()
    for i in range(10000):
        f1.push(i, i*2)
    print()
    # f1.consume()
