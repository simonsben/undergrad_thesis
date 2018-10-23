function result = evaluate_probability(probability)
    %evaluate_probability Evaluates a probability
    %   Evaluates a probability using a uniform distribution

    result = rand() < probability;
end

