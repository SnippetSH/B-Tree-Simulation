// Tree.tsx
import { useEffect, useState, useRef } from 'react';
//import { dict20 } from '../../API/TestSet/test'; //test data
import Block from '../Blocks/Block';
import type { Dict } from '../../API/Types/GETTypes';

export default function Tree({current}: {current: Dict | undefined}) {
  const [depthIdx, setDepthIdx] = useState<number[]>([]);
  const Dict = current;
  const divRef = useRef<HTMLDivElement>(null);


  useEffect(() => { //test useEffect
    if(Dict) {
      const n = Dict["max"];

      const tmp = [...depthIdx];
      for (let i = 0; i < n; i++) {
        tmp.push(0);
      }
      setDepthIdx(tmp);
    }
  }, []);

  useEffect(() => {
    console.log(depthIdx);
  }, [depthIdx]);

  useEffect(() => {
    if(divRef.current) {
      divRef.current.scrollTop = divRef.current.scrollWidth / 2;
    }
  }, [current])

  useEffect(() => {
    const el = divRef.current;
    if (el) {
      const onWheel = (e: WheelEvent) => {
        if (e.deltaY == 0) return;
        e.preventDefault();
        el.scrollTo({
          left: el.scrollLeft + e.deltaY,
          behavior: "smooth"
        });
      };
      el.addEventListener("wheel", onWheel);
      return () => el.removeEventListener("wheel", onWheel);
    }
  }, []);

  const renderTree = (): JSX.Element[] => {
    const depthList: JSX.Element[] = [];
    if(Dict) {
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
    }
    return depthList;
  };

  return (
    <div className='w-5/6 h-3/4 bg-white/20 border-2.5 border-black/35 rounded-3xl overflow-hidden'>
      <div ref={divRef} className='w-full h-full flex flex-col overflow-x-auto overscroll-contain scroll-smooth scrollbar-hide'>
        {current ? renderTree() : null}
      </div>
    </div>
  );
}
