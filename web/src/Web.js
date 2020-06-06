import React from 'react';

function Web(){
      return(
        <div className="app">
  <div className="logo">
    <img src="./logo.png" alt="alna" />
  </div>
  <div className="header">
    <div>
      <h1>НОРМАЛИЗАТОР АДРЕСОВ</h1>
      <p>алгоритм предобработки почтовых адресов</p>
    </div> 
  </div>
  <div className="content">
    <div className="blockFile addFile">
      <div className="h2">
        <h2>Загузить файл</h2>
      </div>
      <div className="span">
        <span>Загрузите файл с ошибочными адресами</span>
      </div>
      <div className="btnAdd btn" id="AddFile">
        <button className="btnAdd btn">Загрузить файл</button>
      </div>
    </div>
    <div className="blockFile getFile">
      <div className="h2">
        <h2>Получить файл</h2>
      </div>
      <div className="span">
        <span>Скачайте полученый файл с исправленными адресами</span>
        </div>
      <div className="btnGet btn" id="getFile">
        <button>Скачать файл</button>
      </div>
    </div>
  </div>
</div>
      )
    }

export default Web;