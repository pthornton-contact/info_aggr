import React from 'react';
import FeedList from "./components/FeedList";

function App() {
  return (
    <div className="bg-gray-50 min-h-screen">
      <header className="bg-blue-500 text-white p-4">
        <h1 className="text-center text-3xl font-bold">Feeds Dashboard</h1>
      </header>
      <main className="container mx-auto py-6">
        <FeedList />
      </main>
    </div>
  );
}

export default App;