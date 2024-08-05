type NestNumberArr = number[][]

interface Dict {
    "max": number,
    [key: number]: NestNumberArr,
}

export type { NestNumberArr, Dict };