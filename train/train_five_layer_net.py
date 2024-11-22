import time
from common.trainer import Trainer
from common.data_loader import load_mnist
from networks.five_layer_net import FiveLayerNet

# 데이터 로드
(x_train, t_train), (x_test, t_test) = load_mnist()

# 5층 신경망 생성
network = FiveLayerNet(input_size=784, 
                      hidden_size1=100,
                      hidden_size2=80,
                      hidden_size3=60,
                      hidden_size4=40,
                      output_size=10)

# 학습 실행
start = time.time()
print(f"시작 시간: {start}")
trainer = Trainer(network, x_train, t_train, x_test, t_test, epochs=100)
end = time.time()
print(f"끝나는 시간:{end}")
print(f"걸린 시간:{end-start}")
trainer.train()
trainer.plot()