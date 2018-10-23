clear;
%% Generate graph
n = 10;  % Number of nodes
connections = zeros(n); % Start with no connections

for i = 1:n % For each row
   for j = i:n % For each column
       connection_sum = sum(connections(:)) + 1; % Sum matrix
       row_sum = sum(connections(:,j)) + 1; % Sum row
       
       if i == n % Don't do self connections
          continue; 
       elseif evaluate_probability(row_sum / connection_sum)
           connections(i, j) = 1;
           connections(j, i) = 1;
       elseif row_sum == 0 && j == n
          connections(i, j) = 1;
          connections(j, i) = 1;
       end
   end
end

%% Plotting
G = graph(connections); % Generate graph
plot(G) % Plot graph