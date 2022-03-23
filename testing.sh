awk '{

print accuracy_mean[$1" "$2];
acc = $4 / 100;
accuracy_mean[$1" "$2] += acc / 5;

accuracy_var[$1" "$2] += acc ^ 2 / (5 - 1);
print accuracy_mean[$1" "$2];
}
END {
for (cond in accuracy_mean) {
mean = accuracy_mean[cond];
std = sqrt(accuracy_var[cond] - mean ^ 2 * 5/ (5 - 1));
# print cond,     mean,        std;
}
}' output/dev.results.txt 
# | sort -n -k 3 > output/dev.results.summary.txt