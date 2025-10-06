import torch

print("script")

#Tensor Creation
x = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
print(x)
print(x.shape)

#Basic Operations
y = x + 10            
z = x * 2          
print("x + 10:\n", y)
print("x * 2:\n", z)


#Tensor Views (reshaping without copy)
view_tensor = x.view(3, 2)
print(view_tensor)

# Modifying view affects original tensor
view_tensor[0][0] = 99
print("Modified\n", view_tensor)
print("Original x after modifying:\n", x)

# Clone (copy tensor)
clone_tensor = x.clone()
clone_tensor[0][0] = -1
print("clone_tensor:\n", clone_tensor)
print("Original x remains:\n", x)

#Broadcasting with different shapes
a = torch.tensor([[1, 2, 3],
                  [4, 5, 6]])
b = torch.tensor([10, 20, 30])  
result = a + b                 
print("a + b (broadcasted):\n", result)
print()

#Moving tensors to GPU (if available)
if torch.cuda.is_available():
    device = torch.device("cuda")
    x_gpu = x.to(device)
    print("x on GPU:", x_gpu)
else:
    print("NOPE")

#Slicing and indexing
print("First row:", x[0])
print("Last column:", x[:, -1])
print()

#Aggregate functions
print("Sum", x.sum())
