#include <stdio.h>
#include <math.h>
int vec(int m,int arr[3]);
int vec(int m,int arr[3]){
    int c;
    c=m/(sqrt(pow(arr[0],2)+pow(arr[1],2)+pow(arr[2],2)));
    arr[0]*=c;
    arr[1]*=c;
    arr[2]*=c;
    printf("B(%d %d %d)",arr[0],arr[1],arr[2]);
}
int main(){
    int m=9;
    int arr[3]={1,-2,2};
    vec(m,arr);
    return 0;
}
