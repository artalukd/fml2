
for DEGREE in 1 2 3 4 5; do
# Test models.
C=$(python -c "print(10)")
echo "c="$C "d="$DEGREE
for SPLIT in 1 2 3 4 5; do
libsvm-3.0/svm-predict output/test.scaled.txt output/model.$C.$DEGREE.$SPLIT.txt output/test.$C.$DEGREE.$SPLIT.prediction.txt 
done
done

