// Tree.tsx
import { useEffect, useState } from 'react';
import { dict100, dict20 } from '../../API/TestSet/test'; //test data
import Block from '../Blocks/Block';

export default function Tree() {
  const [depthIdx, setDepthIdx] = useState<number[]>([]);
  const Dict = dict20;

  useEffect(() => { //test useEffect
    
    const n = Dict["max"];

    const tmp = [...depthIdx];
    for (let i = 0; i < n; i++) {
      tmp.push(0);
    }
    setDepthIdx(tmp);
  }, []);

  useEffect(() => {
    console.log(depthIdx);
  }, [depthIdx]);

  const renderTree = (): JSX.Element[] => {
    const depthList: JSX.Element[] = [];
    for (let depth = 1; depth <= Dict["max"]; depth++) {
      if (!Dict[depth]) continue;

      const divList: JSX.Element[] = [];
      const n = Dict[depth].length;

      for (let i = 0; i < n; i++) {
        divList.push(
          <div key={`${i}of${depth}`} className='flex justify-center'>
            {Dict[depth][i].map(c => (
              <Block k={c} key={c} />
            ))}
          </div>
        );
      }

      depthList.push(
        <div key={`${depth}`} className='w-full flex justify-around m-10'>
          {divList}
        </div>
      );
    }
    return depthList;
  };

  return (
    <div className='w-full h-3/4 bg-lime-400/30'>
      <div className='flex flex-col items-center'>
        {renderTree()}
      </div>
    </div>
  );
}
