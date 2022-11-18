Import torch
Import Torch.Nn As Nn
Import Torch.Nn.Functional As F

# Model configuration
leaky_relu_alpha = 0.1

model = Sequential()
model.add(Conv3D(32, kernel_size=(7,7,7), input_shape=input_shape))
model.add(LeakyReLU(alpha=leaky_relu_alpha))
model.add(MaxPooling3D(pool_size=(2,2,2)))

model.add(Conv3D(64, kernel_size=(5,5,5)))
model.add(LeakyReLU(alpha=leaky_relu_alpha))
model.add(MaxPooling3D(pool_size=(2,2,2)))

model.add(Conv3D(128, kernel_size=(3,3,3)))
model.add(LeakyReLU(alpha=leaky_relu_alpha))
model.add(MaxPooling3D(pool_size=(2,2,2)))

model.add(Conv3D(256, kernel_size=(1,1,1)))
model.add(LeakyReLU(alpha=leaky_relu_alpha))
model.add(MaxPooling3D(pool_size=(2,2,2)))

torch.flatten(model, start_dim=3, end_dim =1)
trd = torch.nn.Linear(model)
y = trd(torch.ones(5, 3))

print(model)
