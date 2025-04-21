#include <stdio.h>

int main(){
    int num;
    scanf("%d", &num);

    int arr[500][500] ={0};
    int count = 1;

    int n;
    for(int i = 1; i <= num; i++){
        while(count <= i){
            scanf("%d", &arr[i - 1][count - 1]);
            count++; 
        }
        count = 1;
    }

    int dp_arr[500][500] = {0};
    dp_arr[0][0] = arr[0][0];
    

    for(int i = 1; i < num; i++){
        while(count <= i){
            if(dp_arr[i - 1][count - 1] + arr[i][count - 1] > dp_arr[i][count - 1]){
                dp_arr[i][count - 1] = dp_arr[i - 1][count - 1] + arr[i][count - 1];
            }
            if(dp_arr[i - 1][count - 1] + arr[i][count] > dp_arr[i][count]){
                dp_arr[i][count] = dp_arr[i - 1][count - 1] + arr[i][count];
            }
            count++; 
        }
        count = 1;
    }

    int max = 0;

    for(int i = 0; i < num; i++){
        if(dp_arr[num - 1][i] > max){
            max = dp_arr[num - 1][i];
        }
    }

    printf("%d\n", max);
    
    return 0;
}