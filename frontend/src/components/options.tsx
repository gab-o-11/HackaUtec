import React, { useState } from 'react';
import { Button, Menu, MenuItem } from '@mui/material';

type Props = {
  onSelect: (option: string) => void;
};

export default function DropdownPanelSelector({ onSelect }: Props) {
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);

  const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = (option?: string) => {
    setAnchorEl(null);
    if (option) {
      onSelect(option); // Envía el valor al padre
    }
  };

  return (
    <>
      <Button
        aria-controls="simple-menu"
        aria-haspopup="true"
        onClick={handleClick}
        sx={{ fontWeight: 'bold', color: 'deeppink' }}
      >
        JSON
      </Button>
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        open={Boolean(anchorEl)}
        onClose={() => handleClose()}
      >
        <MenuItem onClick={() => handleClose('JSON')}>JSON</MenuItem>
        <MenuItem onClick={() => handleClose('E/R')}>E/R</MenuItem>
        <MenuItem onClick={() => handleClose('AWS')}>AWS</MenuItem>
      </Menu>
    </>
  );
}
