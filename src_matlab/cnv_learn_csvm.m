function model = cnv_learn_fitcsvm(predictors,labels,varargin)
% Logistic regression, using specific fields
fields = {'smile_l','smile_r'}; 
vararginoptions(varargin); 
for i=1:length(fields) 
    X(:,i)=predictors.(fields{i}); 
end; 
model.svm = fitcsvm(X,labels,'Standardize',true);
model.fields=fields; 