clear all;
%% Generate graph
n = 10;  % Number of nodes
connections = zeros(n); % Start with no connections

for i = 1:length(connections) % For each row
   for j = 1:(i-1) % For each column
       connection_sum = sum(connections(:)) + 1; % Sum matrix
       row_sum = sum(connections(:,j)) + 1; % Sum row
       
       if i == j % Don't do self connections
          continue; 
       elseif evaluate_probability(row_sum / connection_sum)
           connections(i, j) = 1;
           connections(j, i) = 1;
       elseif row_sum == 0 && j == (i-1)
          connections(i, j) = 1;
          connections(j, i) = 1;
       end
   end
end

%% Plotting
G = graph(connections); % Generate graph
plot(G) % Plot graph