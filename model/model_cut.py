import onnx

onnx_file = "../logs/best_nums.onnx"

model = onnx.load(onnx_file)

nodes = model.graph.node
print(len(nodes))

for i,node in enumerate(nodes):
    print(i , node)

