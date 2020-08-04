clear all;clc;

% Circumference in the Complex Plane
x = linspace(0, 2*pi, 1000000);
p = exp(1i * x);
imagp = imag(p);
realp = real(p);

% Taylor series for e^(pi * i)
tay = zeros(100, 2);
tay(1) = 1;
for k = 2 : 100
    tay(k, 1) = tay(k-1, 1) + real(((sqrt(-1) * pi)^(k-1))/factorial(k-1));
    tay(k, 2) = tay(k-1, 2) + imag(((sqrt(-1) * pi)^(k-1))/factorial(k-1));
end
tay = [zeros(1,2);tay];

% Convergence to -1
plot(realp,imagp,"k-",tay(:,1),tay(:,2),'r-',"LineWidth",2)
axis equal








