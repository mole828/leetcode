function map(arr: number[], fn: (n: number, i: number) => number): number[] {
    const result: number[] = [];
    arr.forEach((value, index)=>{
        result.push(fn(value, index))
    })
    return result;
};
