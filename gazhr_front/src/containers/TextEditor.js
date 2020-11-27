import {Form} from 'react-bootstrap';

function TextEditor({value, onChange}) {
  return (
    <Form.Control
      as="textarea"
      rows={10}
      placeholder={'Введите требования к соискателю'}
      value={value}
      onChange={(event) => onChange(event.target.value)}
    />
  );
}

export default TextEditor;
