import '../../Assets/index.css';
import Tree from './Tree';
import type { Dict } from '../../API/Types/GETTypes';
import { useEffect, useState } from 'react';
import axios from 'axios';

function App() {
  const [current, setCur] = useState<Dict | undefined>({ "max": 0 });
  const [text, setText] = useState('');
  const [val, setVal] = useState(0);

  interface FetchData {
    max: number,
    [key: string]: number | number[][]
  }

  useEffect(() => {
    async function Init() {
      axios.get('init');
    }

    Init();
  }, [])

  const convertKeysToNumbers = (obj: FetchData) => {
    const newObj: Dict = { max: obj.max };
    for (const key in obj) {
      if (obj.hasOwnProperty(key) && key !== 'max') {
        const newKey = Number(key);
        if(newKey === 1 && (obj[key] as number[][]).length > 1) {
          const tmp: number[][] = [[]];
          console.log(obj[key]);
          (obj[key] as number[][]).map((c) => {
            console.log(c);
            tmp[0].push(c[0])
          });
          newObj[newKey] = tmp;
        } else {
          newObj[newKey] = obj[key] as number[][];
        }
      }
    }
    return newObj;
  }

  const modifyInput = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!isNaN(Number(e.target.value))) {
      setVal(Number(e.target.value));
      setText(e.target.value);
    }
  }

  const Traverse = async () => {
    await axios.get<FetchData>('traverse')
      .then(r => {
        let result = convertKeysToNumbers(r.data);
        setCur(result);
      })
      .catch(e => console.log(e));
  }

  const Insert = async () => {
    if (!isNaN(Number(val)) && val !== 0) {
      await axios.post('insert', {
        key: val,
        value: ''
      }).then(() => {
        Traverse();
      }).catch(e => {
        console.log(e);
      })
    }

    setText('');
  }

  const Delete = async () => {
    if (!isNaN(Number(val)) && val !== 0) {
      await axios.post('delete', {
        key: val
      }).then(() => {
        Traverse();
      }).catch(e => console.log(e));
    }

    setText('');
  }

  return (
    <div className='bg-slate-200/80 w-screen h-screen relative flex justify-center items-center'>
      <h1 className='text-black font-bold text-3xl absolute top-7 text-center w-5/6 px-5 pb-3 border-b-2 border-b-slate-600/20'> B tree Simulation </h1>
      <div className='w-full h-5/6 flex items-center justify-center flex-col'>
        <Tree current={current}></Tree>
        <div id="button box" className='flex justify-center my-5 '>
          <input type='text' value={text} onChange={(e) => modifyInput(e)} className='bg-slate-200/80 mx-2 border-2 border-black/40 rounded-md'></input>
          <button onClick={() => Insert()} className="mx-2 w-20 border-1.5 border-black/30 rounded-sm hover:bg-slate-500/40">Insert</button>
          <button onClick={() => Delete()} className="mx-2 w-20 border-1.5 border-black/30 rounded-sm hover:bg-slate-500/40">Delete</button>
        </div>
      </div>
    </div>
  )
}

export default App
