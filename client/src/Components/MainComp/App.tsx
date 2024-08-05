import '../../Assets/index.css';
import Tree from './Tree';

function App() {
  return (
    <div className='bg-slate-200/80 w-screen h-screen relative flex justify-center items-center'>
      <h1 className='text-black font-bold text-3xl absolute top-7 text-center w-5/6 px-5 pb-3 border-b-2 border-b-slate-600/20'> B tree Simulation </h1>
      <Tree></Tree>
    </div>
  )
}

export default App
